#!/bin/bash

# Create 41 users with names from dev1 to dev41, home folders from
# /home/cr-study-2024/dev1 to /home/cr-study-2024/dev40, and random passwords.
# Save users and passwords to a file. Add user to group "cr-study-2024".
# Create Python environment. Update -bashrc file.

RND_PWD="tr -dc 'A-Za-z0-9!\"#$%&'\''()*+,-./:;<=>?@[\]^_\`{|}~' </dev/urandom | head -c 13; echo"
PWD_FILE="users_and_passwords.txt"

rm -f $PWD_FILE
for i in {1..41}
do
    useradd -m -d /home/cr-study-2024/dev$i -s /bin/bash dev$i
    user_pwd="dev$i:$(eval "$RND_PWD")"
    echo "$user_pwd" >> $PWD_FILE
    echo "$user_pwd" | chpasswd
    usermod -aG cr-study-2024 dev$i
    python3.10 -m venv /home/cr-study-2024/dev$i/venv

    {
        echo ""
        echo "# Setup for CR Study 2024"
        echo "export JAVA_HOME=\"/home/cr-study-2024/common/jdk-17.0.10+7\""
        echo "export MAVEN_HOME=\"/home/cr-study-2024/common/apache-maven-3.9.6\""
        echo "export M2_HOME=\$MAVEN_HOME"
        echo "export PATH=\$JAVA_HOME/bin:\$MAVEN_HOME/bin:\$PATH"
        echo "alias python=python3.10"
        echo "source ~/venv/bin/activate"
    } >> /home/cr-study-2024/dev$i/.bashrc
done