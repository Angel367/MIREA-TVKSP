FROM node:20-alpine

# Устанавливаем redis-cli и другие необходимые пакеты
RUN apk add --no-cache redis

WORKDIR /app

# Копируем файл server.js в рабочую директорию
COPY server.js /app

# Устанавливаем зависимости Node.js
RUN npm install redis@3.0.0

# Указываем команду для запуска приложения
CMD ["node", "/app/server.js"]
