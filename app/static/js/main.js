const e = sel => document.querySelector(sel);

/*
 ajax 函数
*/
const ajax = function (method, path, data, responseCallback) {
    let r = new XMLHttpRequest();
    // 设置请求方法和请求地址
    r.open(method, path, true);
    // 设置发送的数据的格式为 application/json
    // 这个不是必须的
    r.setRequestHeader('Content-Type', 'application/json');
    // 注册响应函数
    r.onreadystatechange = function () {
        if (r.readyState === 4) {
            // r.response 存的就是服务器发过来的放在 HTTP BODY 中的数据
            responseCallback(r.response)
        }
    };
    // 把数据转换为 json 格式字符串
    data = JSON.stringify(data);
    // 发送请求
    r.send(data)
};

const apiTodoDelete = id => {
    let path = '/todo/' + id;
    ajax('DELETE', path, {})
};

const bindTodoDelete = () => {
    let todo_list = document.querySelector('#todo-list');
    todo_list.addEventListener('click', event => {
        let self = event.target;
        if (self.classList.contains('button-delete')) {
            let todo_cell = e('.todo-cell');
            let todo_id = todo_cell.dataset.id;
            apiTodoDelete(todo_id);
            todo_cell.remove();
            console.log('delete clicked');
        }
    })
};

const main = () => {
    console.log('js loaded');
    bindTodoDelete();
};

main();