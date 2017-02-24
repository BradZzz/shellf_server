import React from 'react'
import { render } from 'react-dom'
import { createStore, applyMiddleware } from 'redux'
import { Provider } from 'react-redux'
import thunk from 'redux-thunk'
import createLogger from 'redux-logger'
import reducer from './src/reducers'
import App from './src/containers/App'

const middleware = [ thunk ]
if (process.env.NODE_ENV !== 'production') {
  middleware.push(createLogger())
}

const store = createStore(
  reducer,
  applyMiddleware(...middleware)
)

render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
)



//var React = require('react')
//var ReactDOM = require('react-dom')
//
//var ProductItem = React.createClass({
//  render: function () {
//    return (
//      <tr>
//        <td>{this.props.name}</td>
//        <td>{this.props.price}</td>
//      </tr>
//    );
//  }
//});
//
//var ProductList = React.createClass({
//  render: function () {
//    var products = this.props.products.map(function (product, index) {
//      return (
//        <ProductItem
//          key={index}
//          name={product.name}
//          price={product.price}
//        />
//      );
//    });
//
//    return (
//      <table>
//        {products}
//      </table>
//    );
//  }
//});
//
//// Could come from an API, LocalStorage, another component, etc...
//var products = [
//  { name: 'Toast', price: 1499 },
//  { name: 'Bacon', price: 3245 },
//  { name: 'Coffee', price: 300 }
//];
//
//ReactDOM.render(<ProductList products={products} />, document.getElementById('main'));
//
//class ShoppingList extends React.Component {
//  render() {
//    return (
//      <div className="shopping-list">
//        <h1>Shopping List for {this.props.name}</h1>
//        <ul>
//          <li>Instagram</li>
//          <li>WhatsApp</li>
//          <li>Oculus</li>
//        </ul>
//      </div>
//    );
//  }
//}
