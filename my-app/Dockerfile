FROM node:14

WORKDIR /my-app

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the app
COPY . .

# Build the React app
RUN npm run build

# Install serve globally to serve the production build
RUN npm install -g serve

# Expose port 3000 (the port your React app will run on)
EXPOSE 3000

# Set the HOST environment variable to 0.0.0.0 to allow external access
ENV HOST=0.0.0.0

# Serve the production build using serve
CMD ["serve", "-s", "build", "-l", "3000"]
