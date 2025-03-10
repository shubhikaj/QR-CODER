# Use the official Nginx base image
FROM nginx:latest

# Copy the Nginx configuration file into the container
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80 for external access
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]