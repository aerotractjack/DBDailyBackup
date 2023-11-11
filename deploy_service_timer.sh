#!/bin/bash

sudo cp DBDailyBackup.service /etc/systemd/system
sudo cp DBDailyBackup.timer /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable --now DBDailyBackup.timer