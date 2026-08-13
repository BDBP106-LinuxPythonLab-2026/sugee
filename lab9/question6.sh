#1
echo $HOME
#2
bc << EOF
scale=4
23934/44343
EOF

#3
ls $HOME | grep "^D"

#4

grep "$USER" /etc/passwd


