
var chart = c3.generate({
    bindto:"#chart",
    data: {
            url: '/static/json/data.json',
            mimeType: 'json',
            type: 'bar'

        },


});
