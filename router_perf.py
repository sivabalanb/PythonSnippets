import schedule
import time
import ping3
import psutil
import pickle
import logging
from jinja2 import Environment, FileSystemLoader
import subprocess
from pingparsing import PingParsing
import json
# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

metrics_data = []  # List to store collected metrics

def measure_internet_speed():
    try:
        # Use speedtest-cli command-line tool to perform the internet speed test
        speedtest_output = subprocess.check_output(["speedtest-cli", "--json"])
        results_dict = json.loads(speedtest_output)

        metrics_data.append({
            'timestamp': time.time(),
            'type': 'internet_speed',
            'download_speed': results_dict['download'] / 1_000_000,  # Convert to Mbps
            'upload_speed': results_dict['upload'] / 1_000_000      # Convert to Mbps
        })

        logger.info(f"Download Speed: {results_dict['download'] / 1_000_000:.2f} Mbps, "
                    f"Upload Speed: {results_dict['upload'] / 1_000_000:.2f} Mbps")
    except Exception as e:
        logger.error(f"Error measuring internet speed: {e}")

def measure_ping_latency():
    target_server = "www.google.com"  # Replace with a server of your choice
    latency = ping3.ping(target_server)

    metrics_data.append({
        'timestamp': time.time(),
        'type': 'ping_latency',
        'target_server': target_server,
        'latency': latency
    })

    logger.info(f"Ping Latency to {target_server}: {latency} ms")

def measure_system_resources():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent

    metrics_data.append({
        'timestamp': time.time(),
        'type': 'system_resources',
        'cpu_usage': cpu_usage,
        'memory_usage': memory_usage
    })

    logger.info(f"CPU Usage: {cpu_usage}% | Memory Usage: {memory_usage}%")

def save_metrics_to_pickle():
    with open('metrics_data.pkl', 'wb') as f:
        pickle.dump(metrics_data, f)

    logger.info("Metrics data saved to pickle file.")

def save_metrics_to_html():
    template_env = Environment(loader=FileSystemLoader('.'))
    template = template_env.get_template('metrics_report_template.html')

    html_output = template.render(metrics_data=metrics_data)

    with open('metrics_report.html', 'w') as f:
        f.write(html_output)

    logger.info("Metrics data saved to HTML file.")

def main():

    
    # Schedule the monitoring functions to run every 5 minutes
    schedule.every(1).minutes.do(measure_internet_speed)
    schedule.every(1).minutes.do(measure_ping_latency)
    schedule.every(1).minutes.do(measure_system_resources)
    schedule.every(1).hour.do(save_metrics_to_pickle)

    # Schedule the HTML report to be generated once a day
    # schedule.every().day.at("00:00").do(save_metrics_to_html)
    # Schedule the HTML report to be generated every 1 minute for testing
    schedule.every(1).minutes.do(save_metrics_to_html)

    logger.info("Monitoring started.")

    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except KeyboardInterrupt:
            logger.info("Monitoring stopped.")
            break

if __name__ == "__main__":
    main()
