# cURL examples and evidence capture

Start the service in one terminal:
```bash
export FLASK_APP=service
flask run --host=0.0.0.0 --port=8080
```

Use a second terminal. These are example commands; save the actual response from your running app, not a fabricated response.

## CREATE — `rest-create-done`
```bash
curl -i -X POST http://localhost:8080/accounts \
  -H 'Content-Type: application/json' \
  -d '{"name":"Ada Lovelace","email":"ada@example.com","address":"London"}'
```

## LIST — `rest-list-done`
```bash
curl -i http://localhost:8080/accounts
```

## READ — `rest-read-done`
```bash
curl -i http://localhost:8080/accounts/1
```

## UPDATE — `rest-update-done`
```bash
curl -i -X PUT http://localhost:8080/accounts/1 \
  -H 'Content-Type: application/json' \
  -d '{"name":"Ada Byron"}'
```

## DELETE — `rest-delete-done`
```bash
curl -i -X DELETE http://localhost:8080/accounts/1
```

To save a real command and output:
```bash
{ echo 'Command: curl -i http://localhost:8080/accounts'; curl -i http://localhost:8080/accounts; } 2>&1 | tee rest-list-done
```
