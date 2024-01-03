let search = document.getElementById("table-search");


search.addEventListener("click", e => {
    fetch("/", {
        method: "POST",
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            search: Number(e.target.checked)
        })
    })
        .then(res => {
            if (!res.ok) {
                throw Error(JSON.stringify(res.status));
            }

            return res.json();
        })
        .then(({data: {val}}) => {
            console.log(val);
            const res = document.querySelector(".result");
            res.innerText = `client got: ${val}`;
        })
        .catch(err => console.error(err))
    ;
})
