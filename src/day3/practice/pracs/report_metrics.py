def average_order_value(total_revenue, num_orders):
    """Return the average revenue per order for a reporting period."""
    try:
        avg = total_revenue / num_orders
        return round(avg, 2)
    except ArithmeticError as A:
        # print(f" Not divisble by zero")
        return A


def project_revenue(current_revenue, growth_rate, periods):
    """Project revenue compounding at 'growth_rate' over N periods."""
    try:
        projected = current_revenue * (1.0 + growth_rate) ** periods
        return round(projected, 2)
    except(OverflowError,ArithmeticError):
        return "OverflowError in the projection"


# --- Test cases (do not change) ---
print(average_order_value(15000, 120))
print(average_order_value(15000, 0))
print(project_revenue(50000, 0.08, 5))
print(project_revenue(1e6, 8.0, 100000))