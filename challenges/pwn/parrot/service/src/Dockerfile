# Use Debian as the base image (for x86_64 binaries)
FROM debian:bookworm-slim

# Set working directory inside the container
WORKDIR /app

# Install necessary libraries and dependencies (if any)
RUN apt-get update && apt-get install -y libc6

# Copy the ELF binary into the container
COPY server /app/server

# Give execution permissions to the binary
RUN chmod +x /app/server

# Expose a port if needed (optional)
EXPOSE 5001

# Run the ELF binary
CMD ["./server"]