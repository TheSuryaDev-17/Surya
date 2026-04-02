def calculate_gst(amount):
    gst_rate = 0.18  # Assuming GST rate is 18%
    gst = amount * gst_rate
    return gst

# Example usage
if __name__ == '__main__':
    amount = 1000
    print(f'GST on {amount} is: {calculate_gst(amount)}')