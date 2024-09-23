FROM nginx:alpine

# Копируем статические файлы в директорию, откуда NGINX будет их обслуживать
COPY ./static-files /usr/share/nginx/html

# По умолчанию NGINX будет слушать на 80 порту
EXPOSE 80
