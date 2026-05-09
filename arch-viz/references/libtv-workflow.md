# LibTV 鍥剧敓鍥惧伐浣滄祦

閫氳繃libtv API鎵ц寤虹瓚鏁堟灉鍥惧浘鐢熷浘浠诲姟鐨勫畬鏁存祦绋嬨€?
## 鎶€鏈厤缃?
- **Python**锛歚C:\Users\admin\python-sdk\python3.13.2\python.exe`锛堟垨绯荤粺python3锛?- **API Key**锛氶€氳繃鐜鍙橀噺 `LIBTV_ACCESS_KEY` 璁剧疆
- **Base URL**锛歚https://im.liblib.tv`锛堥粯璁わ級

## 鎵ц鍓嶅繀妫€娓呭崟

- [ ] `LIBTV_ACCESS_KEY` 鐜鍙橀噺宸茶缃?- [ ] `change_project.py` 鎵ц鎴愬姛锛岃幏鍙栨柊 projectUuid
- [ ] 搴曞浘涓婁紶鎴愬姛锛岃幏鍙?OSS URL
- [ ] 搴曞浘 URL 鏀惧湪 prompt 鏈€寮€澶?- [ ] `create_session.py` 鎵ц鎴愬姛锛岃幏鍙?sessionId
- [ ] 澧為噺鏌ヨ鑾峰彇鍒版湰娆?task_id
- [ ] 鍥剧墖涓嬭浇鍒版纭洰褰?- [ ] MEDIA 鏍煎紡鍙戦€?- [ ] 鎺ㄩ€佷俊鎭笌鏈鐢熸垚缁撴灉涓€鑷?
---

## 瀹屾暣鎵ц娴佺▼

### Step 1: 鍒囨崲椤圭洰锛堟柊寤虹敾甯冿級

```bash
python3 {baseDir}/scripts/change_project.py
```

**杩斿洖绀轰緥锛?*
```json
{
  "projectUuid": "aa3ba04c5044477cb7a00a9e5bf3b4d0",
  "projectUrl": "https://www.liblib.tv/canvas?projectId=aa3ba04c5044477cb7a00a9e5bf3b4d0"
}
```

**鐩殑锛?* 姣忔浠诲姟蹇呴』鏂板缓椤圭洰鐢诲竷锛岄伩鍏嶅巻鍙插共鎵般€?
---

### Step 2: 涓婁紶搴曞浘

```bash
python3 {baseDir}/scripts/upload_file.py <搴曞浘璺緞>
```

**杩斿洖绀轰緥锛?*
```json
{
  "url": "https://libtv-res.liblib.art/claw/椤圭洰ID/鏂囦欢鍚?jpg"
}
```

---

### Step 3: 鏋勫缓Prompt锛堝叧閿紒锛?
**搴曞浘 URL 蹇呴』鏀惧湪 prompt 鏈€寮€澶达紝鏍煎紡锛?*

```
鍙傝€冨浘鐗囷細https://libtv-res.liblib.art/claw/椤圭洰ID/鏂囦欢鍚?jpg

銆愰噸瑕併€戣涓ユ牸鎸夌収浠ヤ笅瑕佹眰鐢熸垚涓€寮犲浘鐗囷細
锛堝悗缁唴瀹?..锛?```

璇﹁ `prompt-templates.md` 鑾峰彇鎴愬姛prompt妯℃澘銆?
---

### Step 4: 鍒涘缓浼氳瘽骞跺彂閫佷换鍔?
```bash
python3 {baseDir}/scripts/create_session.py "<鏋勫缓鐨刾rompt>"
```

**杩斿洖绀轰緥锛?*
```json
{
  "projectUuid": "aa3ba04c5044477cb7a00a9e5bf3b4d0",
  "sessionId": "90f05e0c-5d08-4148-be40-e30fc7c7bedf",
  "projectUrl": "https://www.liblib.tv/canvas?projectId=aa3ba04c5044477cb7a00a9e5bf3b4d0"
}
```

---

### Step 5: 杞鏌ヨ缁撴灉

```bash
# 棣栨鏌ヨ
python3 {baseDir}/scripts/query_session.py <sessionId> --after-seq 0

# 鍚庣画澧為噺鏌ヨ锛堜娇鐢ㄤ笂娆℃渶澶eq鍊硷級
python3 {baseDir}/scripts/query_session.py <sessionId> --after-seq <涓婃鏈€澶eq>
```

**杞绛栫暐锛?*
- 闂撮殧锛氭瘡 8 绉掓煡璇竴娆?- 瀹屾垚鍒ゆ柇锛歮essages 涓嚭鐜?assistant 娑堟伅涓斿寘鍚浘鐗?瑙嗛 URL
- 瓒呮椂锛氳繛缁?3 鍒嗛挓鏃犵粨鏋滃垯鍋滄

**杩斿洖缁撴瀯锛?*
```json
{
  "messages": [
    {"id": "msg-xxx", "role": "user", "content": "prompt鍐呭"},
    {"id": "msg-yyy", "role": "assistant", "content": "..."}
  ],
  "projectUrl": "https://www.liblib.tv/canvas?projectId=..."
}
```

---

### Step 6: 涓嬭浇缁撴灉

```bash
python3 {baseDir}/scripts/download_results.py <sessionId> --output-dir <涓嬭浇鐩綍> --prefix <鍓嶇紑>
```

**鍙傛暟璇存槑锛?*
- `--output-dir`锛氳緭鍑虹洰褰曪紙榛樿 `~/Downloads/libtv_results/`锛?- `--prefix`锛氭枃浠跺悕鍓嶇紑锛堝 `render_01.png`锛?
**杩斿洖绀轰緥锛?*
```json
{
  "output_dir": "/Users/xxx/Downloads/libtv_results",
  "downloaded": ["/Users/xxx/Downloads/libtv_results/render_01.png"],
  "total": 1
}
```

---

## 鎵归噺澶勭悊锛堝寮犲簳鍥撅級

褰撶敤鎴蜂笂浼犲寮犲簳鍥鹃渶瑕佺敓鎴愭椂锛?
```bash
# 渚濇涓婁紶姣忓紶搴曞浘
python3 {baseDir}/scripts/upload_file.py <搴曞浘1璺緞>
python3 {baseDir}/scripts/upload_file.py <搴曞浘2璺緞>
# ...

# 鍒嗗埆鍒涘缓浼氳瘽锛堟瘡寮犲簳鍥惧崟鐙細璇濓級
python3 {baseDir}/scripts/create_session.py "<鍖呭惈搴曞浘1URL鐨刾rompt>" --session-id <鏂皊essionId>
python3 {baseDir}/scripts/create_session.py "<鍖呭惈搴曞浘2URL鐨刾rompt>" --session-id <鏂皊essionId>
# ...

# 鍒嗗埆杞鍜屼笅杞?```

---

## 閿欒澶勭悊

| 閿欒绫诲瀷 | 澶勭悊鏂瑰紡 |
|----------|----------|
| API 閿欒 (HTTP 4xx/5xx) | 妫€鏌?accessKey 鏄惁姝ｇ‘锛岀綉缁滄槸鍚︽甯?|
| 鏈繑鍥?projectUuid | 閲嶆柊鎵ц change_project.py |
| 鏈繑鍥?sessionId | 閲嶆柊鎵ц create_session.py |
| 杞瓒呮椂 | 鍛婄煡鐢ㄦ埛鍙◢鍚庨€氳繃椤圭洰鐢诲竷閾炬帴鏌ョ湅 |
| 涓嬭浇澶辫触 | 妫€鏌ヨ緭鍑虹洰褰曟潈闄愶紝缃戠粶鏄惁姝ｅ父 |
