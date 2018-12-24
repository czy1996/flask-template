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

const apiTodoAll = callback => {
    let path = '/todo';
    ajax('GET', path, {}, callback);
};

const apiTodoAdd = (data, callback) => {
    let path = '/todo';
    ajax('POST', path, data, callback);
};

const apiTodoUpdate = (id, data, callback) => {
    let path = '/todo/' + id;
    ajax('POST', path, data, callback);
};

const apiTodoDelete = (id, callback) => {
    let path = '/todo/' + id;
    ajax('DELETE', path, {}, callback)
};

let todoTemplate = function (todo) {
    let title = todo.title;
    let id = todo.id;
    // data-xx 是自定义标签属性的语法
    // 通过这样的方式可以给任意标签添加任意属性
    // 假设 d 是 这个 div 的引用
    // 这样的自定义属性通过  d.dataset.xx 来获取
    // 在这个例子里面, 是 d.dataset.id
    let t = `
        <div class="todo-cell" id='todo-${id}' data-id="${id}">
            <span class='todo-title'>${title}</span>
            <button class="todo-delete">x</button>
        </div>
    `;
    return t
};


const insertTodo = todo => {
    let todo_list = document.querySelector('#todo-list');
    todo_list.insertAdjacentHTML('beforeend', todoTemplate(todo));
};

const loadTodos = () => {
    apiTodoAll(r => {
        let todos = JSON.parse(r).data;
        for (let todo of todos) {
            insertTodo(todo);
        }
    })
};

const bindTodoAdd = () => {
    let button = document.querySelector('#id-button-add');
    button.addEventListener('click', event => {
        let title = e('#id-input-todo').value;
        let data = {
            'title': title,
        };
        console.log('clicked add', title);
        apiTodoAdd(data, r => {
            insertTodo(JSON.parse(r).data);
        })
    })
};

const bindTodoDelete = () => {
    let todo_list = document.querySelector('#todo-list');
    todo_list.addEventListener('click', event => {
        let self = event.target;
        if (self.classList.contains('todo-delete')) {
            let todo_cell = self.parentElement;
            let todo_id = todo_cell.dataset.id;
            apiTodoDelete(todo_id);
            todo_cell.remove();
            console.log('delete clicked');
        }
    })
};

const bindTodoUpdate = () => {
    let todo_list = document.querySelector('#todo-list');
    todo_list.addEventListener('click', event => {
        const self = event.target;
        if (self.classList.contains('todo-title')) {
            self.contentEditable = true;
        }
    });

    todo_list.addEventListener('focusout', event => {
        const self = event.target;
        if (self.classList.contains('todo-title')) {
            let newTitle = self.innerText;
            let id = self.parentElement.dataset.id;
            apiTodoUpdate(id, {title: newTitle});
        }
    })
};


const initTodo = () => {
    bindTodoAdd();
    bindTodoDelete();
    bindTodoUpdate();
    loadTodos();
};