$(document).ready(function(){
    $(document).on('click', '.action-btn', function(){
        var getKey = $(this).data('key');
        setResultDetails(getKey);
    });
});

function setResultDetails(key){
    var url = ''
    if(key === 'product'){
        url = "http://localhost:8001/get-products/";
    }
    else if(key === 'order'){
        url = "http://localhost:8002/get-all-order/";
    }
    else if(key === 'invoice'){
        url = "http://localhost:8003/get-all-invoice/";
    }
    if(url) {
        fetch(url)
            .then(response => response.json())
            .then(data => {
                $(".show-result").find("#message").html(data.message);
                $(".show-result").find("#actual-result").html(JSON.stringify(data.data));
            });
    }
}