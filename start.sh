if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/aanzal/ThePro.git /ThePro
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /ThePro
fi
cd /ThePro
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
