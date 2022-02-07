FROM node
WORKDIR /app
COPY package*.json /app
RUN npm install 
COPY index.js /app
EXPOSE 80 
CMD ["node", "index.js"]
