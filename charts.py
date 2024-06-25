# charts.py

def get_chart_data():
    chart_data = {
        'line_chart': {
            'labels': ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
            'data': [65, 59, 80, 81, 56, 55, 40]
        },
        'pie_chart': {
            'labels': ['Red', 'Blue', 'Yellow'],
            'data': [300, 50, 100]
        },
        'bar_chart': {
            'labels': ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
            'data': [65, 59, 80, 81, 56, 55, 40]
        },
        'doughnut_chart': {
            'labels': ['Red', 'Blue', 'Yellow'],
            'data': [300, 50, 100]
        }
    }
    return chart_data
