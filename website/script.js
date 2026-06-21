async function getVisitorCount() {
    const response = await fetch(
        "https://l9b2vf8bi0.execute-api.us-east-1.amazonaws.com/visitor"
    );

    const data = await response.json();

    document.getElementById("visitor-count").innerText =
        data.visitors;
}

getVisitorCount();