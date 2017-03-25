#!/bin/bash
heroku create
git init
git add --all
git commit -m "Initial Commit"
git push heroku master
heroku ps:scale worker=1
echo "Setup complete. Waiting for status ... "
sleep 10
heroku ps
echo "If you see 'worker: crashed' refer README. Otherwise, Tweet@Trump is up!"
