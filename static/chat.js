

function addMessage(text,sender){
    var messageContainer = document.getElementById("messageContainer");
    var messageElement = document.createElement("div");
    messageElement.classList.add("message");
    if(sender === "user"){
        messageElement.classList.add("user-message");
    }
    messageElement.textContent = text;
    messageContainer.appendChild(messageElement);
    messageContainer.scrollTop = messageContainer.scrollHeight;
    
}


function sendMessage(){
    var text = document.getElementById("messageInput").value;
    addMessage(text,"user");
    document.getElementById("messageInput").value = "";
    
}