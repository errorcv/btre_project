var __extends = (this && this.__extends) || (function () {
    var extendStatics = Object.setPrototypeOf ||
        ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
        function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var Button = antd.Button, Modal = antd.Modal, Form = antd.Form, Input = antd.Input, Radio = antd.Radio;
var FormItem = Form.Item;
var CollectionCreateForm = Form.create()(/** @class */ (function (_super) {
    __extends(class_1, _super);
    function class_1() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    class_1.prototype.render = function () {
        var _a = this.props, visible = _a.visible, onCancel = _a.onCancel, onCreate = _a.onCreate, form = _a.form;
        var getFieldDecorator = form.getFieldDecorator;
        return (React.createElement(Modal, { visible: visible, title: "Create a new Job Card", okText: "Create", onCancel: onCancel, onOk: onCreate },
            React.createElement(Form, { layout: "vertical" },
                React.createElement(FormItem, { label: "Company" }, getFieldDecorator('company', {
                    rules: [{ required: true, message: 'Please enter the company name!' }]
                })(React.createElement(Input, null))),
                React.createElement(FormItem, { label: "Job Title" }, getFieldDecorator('job_title', {
                    rules: [{ required: true, message: 'Please enter the job title!' }]
                })(React.createElement(Input, { type: "textarea" }))),
                React.createElement(FormItem, { label: "Application Date (yyyy-mm-dd)" }, getFieldDecorator('applicationdate', {
                    rules: [{ required: true, message: 'Please enter the application date in yyyy-mm-dd format!' }]
                })(React.createElement(Input, null))),
                React.createElement(FormItem, { label: "Please select the status:" }, getFieldDecorator('status', {
                    rules: [{ required: true, message: 'Please select the status!' }], initialValue: 'inprogress'
                })(React.createElement(Radio.Group, null,
                    React.createElement(Radio, { value: "planning" }, "Planning"),
                    React.createElement(Radio, { value: "inprogress" }, "In Progress"),
                    React.createElement(Radio, { value: "success" }, "Success"),
                    React.createElement(Radio, { value: "fail" }, "Fail")))),
                React.createElement(FormItem, { label: "Source" }, getFieldDecorator('source', {
                    rules: [{ required: true, message: 'Please enter the source!' }]
                })(React.createElement(Input, null))))));
    };
    return class_1;
}(React.Component)));
var CollectionsPage = /** @class */ (function (_super) {
    __extends(CollectionsPage, _super);
    function CollectionsPage() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.state = {
            visible: false
        };
        _this.showModal = function () {
            _this.setState({ visible: true });
        };
        _this.handleCancel = function () {
            _this.setState({ visible: false });
        };
        _this.handleCreate = function () {
            var form = _this.formRef.props.form;
            form.validateFields(function (err, values) {
                if (err) {
                    return;
                }

                console.log('Received values of form: ', values);
                form.resetFields();
                _this.setState({ visible: false });
            });
        };
        _this.saveFormRef = function (formRef) {
            _this.formRef = formRef;
        };
        return _this;
    }
    CollectionsPage.prototype.render = function () {
        return (React.createElement("div", null,
            React.createElement(Button, { type: "primary", onClick: this.showModal }, "Add New"),
            React.createElement(CollectionCreateForm, { wrappedComponentRef: this.saveFormRef, visible: this.state.visible, onCancel: this.handleCancel, onCreate: this.handleCreate })));
    };
    return CollectionsPage;
}(React.Component));
ReactDOM.render(React.createElement(CollectionsPage, null), mountNode);