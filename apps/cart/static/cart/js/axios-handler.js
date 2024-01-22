// Cart Page Functions

function getCookie(name) {
   var cookieValue = null;
   if (document.cookie && document.cookie !== "") {
      var cookies = document.cookie.split(";");
      for (var i = 0; i < cookies.length; i++) {
         var cookie = cookies[i].trim();
         if (cookie.substring(0, name.length + 1) === name + "=") {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
         }
      }
   }
   return cookieValue;
}

async function qtyChangeHandler(id, value) {
   let csrftoken = getCookie("csrftoken");
   let data = { qty: value, pk: id };
   axios.defaults.xsrfCookieName = "csrftoken";
   axios
      .put(`/checkout/handle-cart/${id}/`, data, {
         headers: {
            "X-CSRFToken": csrftoken,
         },
      })
      .then((res) => {
         if (res.status === 200) {
            let list = document.querySelectorAll(".cart_item_tag");
            for (index in list) {
               if (list[index].id === id && value === "0") {
                  list[index].remove();
               }
            }
            document.getElementById("cartTotalPrice").innerHTML =
               res.data.cart_price.toLocaleString("fa-IR");
            document.getElementById(`cartItemPrice-${id}`).innerHTML =
               res.data.cart_item_price.toLocaleString("fa-IR");
         }
      })
      .catch((err) => {
         console.log(err);
      });
}

async function deleteItemHandler(id) {
   var csrftoken = getCookie("csrftoken");
   axios.defaults.xsrfCookieName = "csrftoken";
   axios
      .delete(`/checkout/handle-cart/${id}/`, {
         data: { pk: id },
         headers: { "X-CSRFToken": csrftoken },
      })
      .then((res) => {
         if (res.status === 200) {
            let list = document.querySelectorAll(".cart_item_tag");
            for (index in list) {
               if (list[index].id == res.data.pk) {
                  list[index].remove();
               }
            }
            document.getElementById("cartTotalPrice").innerHTML =
               res.data.cart_price.toLocaleString("fa-IR");
         }
      })
      .catch((err) => {
         console.log(err);
      });
}

// Shipping Page Functions

async function applyDiscountCode(data) {
   let codeInput = document.querySelector("#discountCodeInput");
   let csrftoken = getCookie("csrftoken");
   axios.defaults.xsrfCookieName = "csrftoken";
   axios
      .post(
         `/checkout/apply-discount-code/`,
         { code: codeInput.value },
         { headers: { "X-CSRFToken": csrftoken } }
      )
      .then((res) => {
         if (res.status === 200) {
            console.log(res.data);
            // document.getElementById("cartTotalPrice").innerHTML =
            //    res.data.cart_price.toLocaleString("fa-IR");
            // document.getElementById(`cartItemPrice-${id}`).innerHTML =
            //    res.data.cart_item_price.toLocaleString("fa-IR");
         }
      })
      .catch((err) => {
         console.log(err);
      });
}

async function addressSelectFun(id) {
   axios
      .post(
         `/checkout/handle-address/`,
         { pk: id },
         { headers: { "X-CSRFToken": getCookie("csrftoken") } }
      )
      .then((res) => {
         if (res.status === 204) {
            document.querySelector(`#address-${id}`).className =
               "addressSelector border border-2 rounded my-3 p-3";
         }
         if (res.status === 200) {
            let addrs = document.querySelectorAll(".addressSelector");
            for (const addr of addrs) {
               addr.classList.remove("text-success", "border-success");
               if (addr.id == `address-${id}`) {
                  addr.classList.add("text-success", "border-success");
               }
            }
         }
      })
      .catch((err) => {
         console.log(err);
      });
}

async function ShippingMethodSelect(method) {
   axios.defaults.xsrfCookieName = "csrftoken";
   axios
      .post(
         `/checkout/handle-shipping-method/`,
         { method },
         { headers: { "X-CSRFToken": getCookie("csrftoken") } }
      )
      .then((res) => {
         if (res.status === 200) {
            let methods = document.querySelectorAll(".shippingSelector");
            for (const item of methods) {
               item.classList.remove("text-success", "border-success");
               if (item.id == `shipping_method_${method}`) {
                  item.classList.add("text-success", "border-success");
               }
            }
         }
      })
      .catch((err) => {
         console.log(err);
      });
}

// Payment Page Functions

async function createOrder() {
   axios.defaults.xsrfCookieName = "csrftoken";
   axios
      .post(
         `/checkout/handle-order/`,
         {},
         { headers: { "X-CSRFToken": getCookie("csrftoken") } }
      )
      .then((res) => {
         if (res.status === 201) {
            window.location.href = "http://localhost/checkout/thank-you/";
         }
      })
      .catch((err) => {
         console.log(err);
      });
}
// Other Functions For All Pages

let num = document.querySelectorAll(".en_to_fa_number");
("toPersianNumber");
for (index in num) {
   num[index].innerHTML = parseInt(num[index].innerHTML).toLocaleString(
      "fa-IR"
   );
}
