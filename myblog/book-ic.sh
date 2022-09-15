#! /bin/sh
cd /
cd ../var/www/book-ic/
#rm -r blog-java
#git clone https://github.com/kati5211/blog-java.git
systemctl reload apache2
cd blog-java
chmod 777 myblog
cd myblog
chmod 777 blog
chmod 777 db.sqlite3
