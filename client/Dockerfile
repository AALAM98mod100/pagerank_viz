# Stage 1: Install dependencies
FROM node:lts-bullseye AS deps

WORKDIR /frontend

COPY package.json package-lock.json ./
RUN npm install

# Stage 2: Copy dependencies and source code
FROM node:lts-bullseye

WORKDIR /frontend

COPY --from=deps /frontend/node_modules ./node_modules
COPY . .

EXPOSE 3000

CMD ["npm", "start"]