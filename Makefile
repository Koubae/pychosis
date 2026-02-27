
sync:
	git pull; git status; git add .; git commit -a -m "Sync changes"; git push; printf "\n\n🔎 Checking Sync Status.... 🪄\n"; git status;

sync-experiments:
	git pull; git status; git add ./experiments; git commit -a -m "Sync Experiment 🧪 changes"; git push; printf "\n\n🔎 Checking Sync Status (Experiment 🧪).... 🪄\n"; git status;
