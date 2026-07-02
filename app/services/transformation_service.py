from app.services.llm_service import call_llm
from app.utils.prompt_loader import load_prompt_template
from app.utils.cache import get_cache, set_cache
import json
import hashlib
from concurrent.futures import ThreadPoolExecutor

BATCH_SIZE = 10
MAX_WORKERS = 4

IMPORTANT_COLUMNS = [
    "name", "ipAddress", "model", "network",
    "status", "longitude", "latitude",
    "city", "state", "site", "location_type"
]

def join_data(device_df, location_df):
    return device_df.merge(
        location_df,
        left_on="location_id",
        right_on="id",
        how="left"
    )

def filter_columns(row):
    return {k: row[k] for k in IMPORTANT_COLUMNS if k in row}

def split_batches(df, batch_size):
    return [df.iloc[i:i + batch_size] for i in range(0, len(df), batch_size)]

def build_batch_prompt(rows, template):
    data = [filter_columns(row) for _, row in rows.iterrows()]
    return template.replace("{input_data}", json.dumps(data))

def parse_llm_output(output):
    try:
        return json.loads(output)
    except:
        return [{"raw_output": output}]

def hash_data(data):
    return hashlib.md5(str(data).encode()).hexdigest()

def process_batch(batch, template):
    key = hash_data(batch.to_dict())

    cached = get_cache(key)
    if cached:
        return cached

    prompt = build_batch_prompt(batch, template)

    try:
        output = call_llm(prompt)
        parsed = parse_llm_output(output)

        set_cache(key, parsed)
        return parsed
    except Exception as e:
        return [{"error": str(e)}]

def transform_data(merged_df):
    template = load_prompt_template()
    batches = split_batches(merged_df, BATCH_SIZE)

    results = []

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        responses = executor.map(
            lambda batch: process_batch(batch, template),
            batches
        )

    for r in responses:
        results.extend(r if isinstance(r, list) else [r])

    return results