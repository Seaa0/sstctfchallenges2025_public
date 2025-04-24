# Use the official NGINX image
FROM nginx:alpine

# Copy your custom config
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy HTML files to NGINX html folder
COPY . /usr/share/nginx/html

# Expose port 7001
EXPOSE 7001

# Start NGINX server
CMD ["nginx", "-g", "daemon off;"]