// i am facing a problem where when i logged in and then back to the login page again 
// and login normally it says forbidden and needs to reload the page.
// so to solve this:  

/*
This JavaScript approach listens for the pageshow event, which fires when a page is shown, including when navigating back.

event.persisted: This property indicates whether the page is being loaded from the browser's cache. If it's true, 
the page was likely restored from the cache when the user hit the back button.
*/
window.addEventListener("pageshow", function(event) {
    if (event.persisted) {
      window.location.reload();
    }
  });

