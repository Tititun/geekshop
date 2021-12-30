window.onload = function () {
    let quantity, price, orderitem_num, delta_quantity, orderitem_quantity, delta_cost;

    let quantity_arr = [];
    let price_arr = [];

    let total_forms = parseInt($('input[name=orderitems-TOTAL_FORMS]').val())

    let order_total_quantity = parseInt($('.order_total_quantity').text()) || 0;
    let order_total_cost = parseInt($('.order_total_cost').text().replace(',', '.')) || 0;

    for (let i = 0; i < total_forms; i++) {
        let quantity = parseInt($(`input[name=orderitems-${i}-quantity`).val());
        let price = parseInt($(`.orderlist-${i}-price`).text().replace(',', '.'));

        quantity_arr[i] = quantity;
        if (price) {
            price_arr[i] = price;
        } else {
            price_arr[i] = 0;
        }
    }

    $('.order_form').on('click', 'input[type=number]', function () {
          let target = event.target;
          orderitem_num = parseInt(target.name.replace('orderitems-' ,'').replace('-quantity', ''));
          if(price_arr[orderitem_num]) {
              orderitem_quantity = parseInt(target.value);
              delta_quantity = orderitem_quantity - quantity_arr[orderitem_num];
              quantity_arr[orderitem_num] = orderitem_quantity;
              orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
              priceUpdate(orderitem_num);
          }
    });

    $('.order_form').on('click', 'input[type=checkbox]', function () {
          let target = event.target;
          orderitem_num = parseInt(target.name.replace('orderitems-' ,'').replace('-DELETE', ''));
          if(target.checked) {
              delta_quantity =- quantity_arr[orderitem_num]}
          else {
              delta_quantity = quantity_arr[orderitem_num];
            }
          orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
    });

    function orderSummaryUpdate (orderitem_price, delta_quantity) {
        delta_cost = orderitem_price * delta_quantity;
        order_total_cost = Number((order_total_cost + delta_cost).toFixed(2));
        order_total_quantity = order_total_quantity + delta_quantity;
        $('.order_total_quantity').html(order_total_quantity.toString());
        $('.order_total_cost').html(order_total_cost.toString() + ',00');
    }

    function priceUpdate (item_id) {
        let text = quantity_arr[item_id] * price_arr[item_id] + ' руб';
        $(`.orderlist-${item_id}-price`).text(text);
    }

    $('.formset_row').formset({
        addText: 'добавить продукт',
        deleteText: 'удалить',
        prefix: 'orderItems',
        removed: deleteOrderItem,
    })

    function deleteOrderItem(row){
        let target_name = row[0].querySelector('input[type="number"]').name;
        orderitem_num = parseInt(target_name.replace('orderitems-', '').replace('-quantity', ''));
        delta_quantity = -quantity_arr[orderitem_num];
        orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
    }
}