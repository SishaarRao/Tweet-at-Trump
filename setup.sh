#!/bin/bash
heroku create
git init
git add --all
git commit -m "Initial Commit"
git push heroku master
heroku ps:scale worker=1
sleep 5
heroku ps
echo "Setup complete. If you see 'worker: crashed' refer README"
