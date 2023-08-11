var ctx = document.getElementById('combinedchart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: [
          {% for item in total_labels %}
            "{{ item }}",
          {% endfor %}
        ],

        datasets: [{
            label: 'Long/Short Trades',
            backgroundColor: 'rgba(169,187,200,0.2)',
            borderColor: 'rgba(169,187,200,1)',
            borderWidth: 1,
            data: [
              {% for item in total_trades %}
                "{{ item }}",
              {% endfor %}
            ]

        }, {

            label: 'Long/Short Pnl',
            backgroundColor: 'rgba(65,105,225,0.2)',
            borderColor: 'rgba(65,105,225,1)',
            borderWidth: 1,
            data: [
              {% for item in total_pnl %}
                "{{ item }}",
              {% endfor %}
            ]
        }]
    },

    // Configuration options go here
    options: {

    }
});