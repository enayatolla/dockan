// Toggle mobile menu drawer navigation
const mobileMenuDrawerNavigationButton = document.getElementById("mobile-menu-drawer-navigation-button");
const mobileMenuDrawerNavigation = document.getElementById("mobile-menu-drawer-navigation");
const mobileMenuDrawerBackdrop = document.getElementById("mobile-menu-drawer-backdrop");
const mobileMenuDrawerNavigationCloseButton = document.getElementById("mobile-menu-drawer-navigation-close-button");
mobileMenuDrawerNavigationButton.addEventListener("click", function () {
   if (mobileMenuDrawerNavigation.classList.contains("translate-x-full")) {
      mobileMenuDrawerNavigation.classList.remove("translate-x-full");
      mobileMenuDrawerBackdrop.classList.remove("hidden");
   } else {
      mobileMenuDrawerNavigation.classList.add("translate-x-full");
      mobileMenuDrawerBackdrop.classList.add("hidden");
   }
});
mobileMenuDrawerBackdrop.addEventListener("click", function () {
   mobileMenuDrawerBackdrop.classList.add("hidden");
   mobileMenuDrawerNavigation.classList.add("translate-x-full");
});
mobileMenuDrawerNavigationCloseButton.addEventListener("click", function () {
   mobileMenuDrawerBackdrop.classList.add("hidden");
   mobileMenuDrawerNavigation.classList.add("translate-x-full");
});
