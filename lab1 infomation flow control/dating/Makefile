dating-server:
	$(TROUPE)/bin/troupec dating-server.trp -o ./out/dating-server.js
	node $(TROUPE)/rt/built/troupe.js -f=./out/dating-server.js --id=../ids/id-server.json --trustmap=../trustmaps/GoT.json --aliases=aliases.json

malicious-a:
	$(TROUPE)/bin/troupec malicious-a.trp -o ./out/malicious-a.js
	node $(TROUPE)/rt/built/troupe.js -f=./out/malicious-a.js --id=../ids/id-client-alice.json  --trustmap=../trustmaps/client.json

malicious-b:
	$(TROUPE)/bin/troupec malicious-b.trp -o ./out/malicious-b.js
	node $(TROUPE)/rt/built/troupe.js -f=./out/malicious-b.js --id=../ids/id-client-bob.json  --trustmap=../trustmaps/client.json

malicious-c:
	$(TROUPE)/bin/troupec malicious-c.trp -o ./out/malicious-c.js
	node $(TROUPE)/rt/built/troupe.js -f=./out/malicious-c.js --id=../ids/id-client-carl.json  --trustmap=../trustmaps/client.json

malicious-d:
	$(TROUPE)/bin/troupec malicious-d.trp -o ./out/malicious-d.js
	node $(TROUPE)/rt/built/troupe.js -f=./out/malicious-d.js --id=../ids/id-client-delft.json  --trustmap=../trustmaps/client.json

benile-a:
	$(TROUPE)/bin/troupec benile-a.trp -o ./out/benile-a.js
	node $(TROUPE)/rt/built/troupe.js -f=./out/benile-a.js --id=../ids/id-client-alice.json  --trustmap=../trustmaps/client.json