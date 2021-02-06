$(document).ready(function(){
    $(document).on('click', '.action-btn', function(){
        var getKey = $(this).data('key');
        setResultDetails(getKey);
    });
});

function setResultDetails(key){
    var url = ''
    if(key === 'product'){
        url = "http://127.0.0.1/product/get-products/";
    }
    else if(key === 'order'){
        url = "http://127.0.0.1/order/get-all-order/";
    }
    else if(key === 'invoice'){
        url = "http://127.0.0.1/invoice/get-all-invoice/";
    }
    else if(key == 'nodejs'){
        url = "http://127.0.0.1/help/get-all-help/";
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