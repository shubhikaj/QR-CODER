# Use the Node.js official image
FROM node:20

# Set working directory inside the container
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json package-lock.json ./
RUN npm install --legacy-peer-deps

# install serve
RUN npm install -g serve

# Copy the rest of the frontend code
COPY . .

# Build the frontend
RUN npm run build

# Expose the port React uses
EXPOSE 3000

# Start the frontend server
CMD ["serve", "-s", "build", "-l", "3000"]