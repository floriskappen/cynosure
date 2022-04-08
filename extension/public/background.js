
// Tab change
// Only submit an event after 5sec of it being active
chrome.tabs.onActivated.addListener(async (activeTabInfo) => {
    if (activeTabInfo.tabId) {
        const tabInfo = await chrome.tabs.get(activeTabInfo.tabId)
        console.log(tabInfo)
    }
})

// Out of focus - send IDLE
chrome.windows.onFocusChanged.addListener(function(window) {
    if (window == chrome.windows.WINDOW_ID_NONE) {
        console.log("out of focus")
    } else {
        console.log("in focus")
    }
});

// TODO: Keep track of all user input to check if idle, etc. Maybe also keep track of actions per minute



