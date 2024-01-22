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

async function changeNameHandler() {
   let firstName = document.querySelector("#inputFirstName").value;
   let lastName = document.querySelector("#inputLastName").value;

   let FirstNameHTML = document.querySelector("#FirstNameHTML");
   let LastNameHTML = document.querySelector("#LastNameHTML");

   let csrftoken = getCookie("csrftoken");
   axios.defaults.xsrfCookieName = "csrftoken";
   axios
      .post(
         "/users/change-fullname/",
         { firstName, lastName },
         {
            headers: {
               "X-CSRFToken": csrftoken,
            },
         }
      )
      .then((res) => {
         console.log(res.data);
         if (res.status === 200) {
            let textName = document.querySelector("#nameChangeInputText");
            textName.innerHTML = "نام ثبت شد پنجره را ببندید";
            textName.className =
               "text-success bg-success-subtle border border-success p-2 mb-3 text-center rounded";
            FirstNameHTML.innerHTML = firstName;
            LastNameHTML.innerHTML = lastName;
         }
      })
      .catch((error) => {
         if (error.response.status === 400) {
            let textName = document.querySelector("#nameChangeInputText");
            textName.innerHTML = error.response.data.msg;
            textName.className =
               "text-danger bg-danger-subtle border border-danger p-2 mb-2 text-center rounded";
         }
      });
}

async function otpRequestHandler() {
   let phoneNumber = document.querySelector("#InputphoneNumber").value;

   let csrftoken = getCookie("csrftoken");
   axios.defaults.xsrfCookieName = "csrftoken";
   axios
      .post(
         "/users/change-phonenumber/",
         { phoneNumber },
         {
            headers: {
               "X-CSRFToken": csrftoken,
            },
         }
      )
      .then((res) => {
         console.log(res.data);
         if (res.status === 200) {
            let textName = document.querySelector("#otpRequestTextGuide");
            textName.innerHTML = "رمز یکبار مصرف را وارد کنید";
            textName.className =
               "text-info bg-info-subtle border border-info p-2 mb-3 text-center rounded";
            document
               .querySelector("#otpCheckInputWrapper")
               .classList.remove("d-none");
            document
               .querySelector("#otpRequestFormBtn")
               .classList.add("d-none");
            document
               .querySelector("#otpCheckFormBtn")
               .classList.remove("d-none");
            document.querySelector("#inputOtpIdHolder").value = res.data.otp_id;
         }
      })
      .catch((error) => {
         if (error.response.status === 400) {
            console.log(error.response.data.msg);
            let textName = document.querySelector("#otpRequestTextGuide");
            textName.innerHTML = error.response.data.msg;
            textName.className =
               "text-danger bg-danger-subtle border border-danger p-2 mb-2 text-center rounded";
         }
      });
}

async function otpCheckHandler() {
   let phoneNumber = document.querySelector("#InputphoneNumber").value;
   let phoneNumberHTML = document.querySelector("#phoneNumberHTML");
   let otpId = document.querySelector("#inputOtpIdHolder").value;
   let otpCode = document.querySelector("#InputOtpCode").value;

   let csrftoken = getCookie("csrftoken");
   axios.defaults.xsrfCookieName = "csrftoken";
   axios
      .put(
         "/users/change-phonenumber/",
         { phoneNumber, otpId, otpCode },
         {
            headers: {
               "X-CSRFToken": csrftoken,
            },
         }
      )
      .then((res) => {
         if (res.status === 200) {
            let textName = document.querySelector("#otpRequestTextGuide");
            textName.innerHTML = "تغییر تلفن اعمال شد پنجره را ببندید";
            textName.className =
               "text-success bg-success-subtle border border-success p-2 mb-3 text-center rounded";
            phoneNumberHTML.innerHTML = phoneNumber;

            document
               .querySelector("#phoneInputWrapper")
               .classList.add("d-none");
            document
               .querySelector("#otpCheckInputWrapper")
               .classList.add("d-none");
            document.querySelector("#otpCheckFormBtn").classList.add("d-none");
         }
      })
      .catch((error) => {
         if (error.response.status === 400) {
            let textName = document.querySelector("#otpRequestTextGuide");
            textName.innerHTML = error.response.data.msg;
            textName.className =
               "text-danger bg-danger-subtle border border-danger p-2 mb-2 text-center rounded";
         }
      });
}

async function changeEmailHandler() {
   let email = document.querySelector("#emailChangeInput").value;

   let csrftoken = getCookie("csrftoken");
   axios.defaults.xsrfCookieName = "csrftoken";
   axios
      .post(
         "/users/change-email/",
         { email: email },
         {
            headers: {
               "X-CSRFToken": csrftoken,
            },
         }
      )
      .then((res) => {
         if (res.status === 200) {
            let err = document.querySelector("#emailChangeInputText");
            err.innerHTML = "ایمیل ثبت شد پنجره را ببندید";
            err.className =
               "text-success bg-success-subtle border border-success p-2 mb-3 text-center rounded";
         }
      })
      .catch((error) => {
         if (error.response.status === 400) {
            let err = document.querySelector("#emailChangeInputText");
            err.innerHTML = error.response.data.msg;
            err.className =
               "text-danger bg-danger-subtle border border-danger p-2 mb-2 text-center rounded";
         }
      });
}

async function createAddress() {
   let province = document.querySelector("#inputAddress-1").value;
   let city = document.querySelector("#inputAddress-2").value;
   let address = document.querySelector("#inputAddress-3").value;
   let region = document.querySelector("#inputAddress-4").value;
   let last = document.querySelector("#inputAddress-5").value;
   let plaque = document.querySelector("#inputAddress-6").value;
   let postal_code = document.querySelector("#inputAddress-7").value;
   let stairs = document.querySelector("#inputAddress-8").value;
   let phone = document.querySelector("#inputAddress-9").value;

   console.log(
      province,
      city,
      address,
      region,
      last,
      plaque,
      postal_code,
      stairs,
      phone
   );

   let csrftoken = getCookie("csrftoken");
   axios.defaults.xsrfCookieName = "csrftoken";
   axios
      .post(
         "/users/handle-address/",
         {
            province,
            city,
            address,
            region,
            last,
            plaque,
            postal_code,
            stairs,
            phone,
         },
         {
            headers: {
               "X-CSRFToken": csrftoken,
            },
         }
      )
      .then((res) => {
         if (res.status === 200) {
            console.log(res.data);
            let textGuide = document.querySelector("#addressTextGuide");
            textGuide.innerHTML = "آدرس زخیره شد. لطفا صفحه را ببندید";
            textGuide.className =
               "text-success bg-success-subtle border border-success p-2 mb-3 text-center rounded";
         }
      })
      .catch((error) => {
         if (error.response.status === 400) {
            console.log(error.response.data.msg);
         }
      });
}

function deleteAddress(pk) {
   let csrftoken = getCookie("csrftoken");
   axios.defaults.xsrfCookieName = "csrftoken";
   axios
      .delete("/users/handle-address/", {
         data: { id: pk },
         headers: { "X-CSRFToken": csrftoken },
      })
      .then((res) => {
         if (res.status === 200) {
            console.log(res.data);
            let addrList = document.querySelectorAll(".addressItem");
            for (index in addrList) {
               if (addrList[index].id == pk) {
                  addrList[index].remove();
               }
            }
            // let textGuide = document.querySelector("#addressTextGuide");
            // textGuide.innerHTML = "";
            // textGuide.className =
            //    "text-success bg-success-subtle border border-success p-2 mb-3 text-center rounded";
         }
      })
      .catch((error) => {
         if (error.response.status === 400) {
            console.log(error.response.data.msg);
         }
      });
}
