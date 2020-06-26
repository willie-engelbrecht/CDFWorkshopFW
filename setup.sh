echo "Installing dependencies..."
yum -y install unzip uwsgi.x86_64 uwsgi-plugin-python36.x86_64 python36-requests.noarch git
pip3 install flask

cd /opt
git clone https://github.com/willie-engelbrecht/CDFWorkshopFW
mv CDFWorkshopFW registration

cd /opt/registration
cp registration.conf /etc/nginx/conf.d/registration.conf
cp registration.service /etc/systemd/system/registration.service
systemctl enable registration.service
systemctl start registration.service
sudo systemctl restart nginx

clear
read -p "AWS Access Key: " AWS_ACCESS
read -p "AWS Secret Key: " AWS_SECRET
read -p "Security Group 1: " SG1
read -p "Security Group 2: " SG2
read -p "Workshop Keyword: " WKEY

echo ${SG1} > /etc/sg1
echo ${SG2} > /etc/sg2
echo ${WKEY} > /etc/wkey

rm -rf aws
curl -s "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip

aws/install

mkdir /root/.aws 2> /dev/null
mkdir /var/lib/nginx/.aws 2> /dev/null

cat > /root/.aws/config << EOF
[default]
aws_access_key_id = ${AWS_ACCESS}
aws_secret_access_key = ${AWS_SECRET}
EOF

cat /root/.aws/config > /var/lib/nginx/.aws/config

echo ""
echo "You can now browse to: http://$(curl -s ipinfo.io/hostname):8080"
echo ""
