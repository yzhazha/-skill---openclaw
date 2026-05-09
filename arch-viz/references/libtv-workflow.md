# LibTV Image-to-Image Workflow

Complete workflow for architectural render image-to-image tasks via LibTV API.

## Technical Configuration

- **Python**: Python 3 (system python3)
- **API Key**: Set via `LIBTV_ACCESS_KEY` environment variable
- **Base URL**: `https://im.liblib.tv` (default)

## Pre-Check List

- [ ] `LIBTV_ACCESS_KEY` environment variable is set
- [ ] `change_project.py` executed successfully, new projectUuid obtained
- [ ] Base image uploaded successfully, OSS URL obtained
- [ ] Base image URL at prompt beginning
- [ ] `create_session.py` executed successfully, sessionId obtained
- [ ] Incremental query obtained this task_id
- [ ] Image downloaded to correct directory
- [ ] MEDIA format sent
- [ ] Push info matches this generation result

---

## Complete Workflow

### Step 1: Switch Project (New Canvas)

```bash
python3 {baseDir}/scripts/change_project.py
```

**Returns:**
```json
{
  "projectUuid": "aa3ba04c5044477cb7a00a9e5bf3b4d0",
  "projectUrl": "https://www.liblib.tv/canvas?projectId=aa3ba04c5044477cb7a00a9e5bf3b4d0"
}
```

**Purpose:** Each task must create new project canvas to avoid history interference.

---

### Step 2: Upload Base Image

```bash
python3 {baseDir}/scripts/upload_file.py <base-image-path>
```

**Returns:**
```json
{
  "url": "https://libtv-res.liblib.art/claw/projectId/filename.jpg"
}
```

---

### Step 3: Build Prompt (Key!)

**Base image URL must be at prompt beginning, format:**

```
Reference image: https://libtv-res.liblib.art/claw/projectId/filename.jpg

[Important] Please strictly generate an image according to the following requirements:
(follow-up content...)
```

See `prompt-templates.md` for successful prompt templates.

---

### Step 4: Create Session and Send Task

```bash
python3 {baseDir}/scripts/create_session.py "<built prompt>"
```

**Returns:**
```json
{
  "projectUuid": "aa3ba04c5044477cb7a00a9e5bf3b4d0",
  "sessionId": "90f05e0c-5d08-4148-be40-e30fc7c7bedf",
  "projectUrl": "https://www.liblib.tv/canvas?projectId=aa3ba04c5044477cb7a00a9e5bf3b4d0"
}
```

---

### Step 5: Poll for Results

```bash
# First query
python3 {baseDir}/scripts/query_session.py <sessionId> --after-seq 0

# Subsequent incremental queries (use last max seq value)
python3 {baseDir}/scripts/query_session.py <sessionId> --after-seq <last max seq>
```

**Polling Strategy:**
- Interval: Query every 8 seconds
- Completion: Assistant message with image/video URL appears in messages
- Timeout: Stop after 3 minutes with no result

**Returns:**
```json
{
  "messages": [
    {"id": "msg-xxx", "role": "user", "content": "prompt content"},
    {"id": "msg-yyy", "role": "assistant", "content": "..."}
  ],
  "projectUrl": "https://www.liblib.tv/canvas?projectId=..."
}
```

---

### Step 6: Download Results

```bash
python3 {baseDir}/scripts/download_results.py <sessionId> --output-dir <download-dir> --prefix <prefix>
```

**Parameters:**
- `--output-dir`: Output directory (default `~/Downloads/libtv_results/`)
- `--prefix`: Filename prefix (e.g., `render_01.png`)

**Returns:**
```json
{
  "output_dir": "/Users/xxx/Downloads/libtv_results",
  "downloaded": ["/Users/xxx/Downloads/libtv_results/render_01.png"],
  "total": 1
}
```

---

## Batch Processing (Multiple Base Images)

When user uploads multiple base images:

```bash
# Upload each base image
python3 {baseDir}/scripts/upload_file.py <base-image-1-path>
python3 {baseDir}/scripts/upload_file.py <base-image-2-path>
# ...

# Create separate sessions for each
python3 {baseDir}/scripts/create_session.py "<prompt with base image 1 URL>" --session-id <new sessionId>
python3 {baseDir}/scripts/create_session.py "<prompt with base image 2 URL>" --session-id <new sessionId>
# ...

# Poll and download separately
```

---

## Error Handling

| Error Type | Handling |
|------------|----------|
| API Error (HTTP 4xx/5xx) | Check if accessKey is correct, network is normal |
| No projectUuid returned | Re-execute change_project.py |
| No sessionId returned | Re-execute create_session.py |
| Poll timeout | Inform user to check project canvas link |
| Download failed | Check output directory permissions, network is normal |
