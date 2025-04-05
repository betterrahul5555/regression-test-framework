def test_log_contains_success():
  with open("logs/sample_log.txt","r") as f:
    logs = f.read()
  assert "Operation complited successfully" in logs
