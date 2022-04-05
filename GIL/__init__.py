# GIL: global interpreter lock
# 同一時刻只允許一個thread在cpu上執行
# GIL會根據執行字節碼行數及時間片段釋放GIL，或遇到IO操作時主動釋放
