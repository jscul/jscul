# [JavaScript](https://github.com/jscul/js/edit/master/README.md) [⚙️](https://github.com/jscul/js/edit/master/config.json)
Common and useful JavaScript modules

## Testing
```javascript
// this will only run if calling `node file.js` directly.
if (typeof require !== 'undefined' && require.main === module) {
	func();
}
```

## Links

### Common

1. Style guide: https://github.com/airbnb/javascript
1. Promise chaining: https://javascript.info/promise-chaining
1. Common functions: https://codeburst.io/useful-javascript-array-and-object-methods-6c7971d93230
1. npm package publishing: https://docs.npmjs.com/getting-started/publishing-npm-packages
1. Electron apps: https://electronjs.org/
1. npm package: https://itnext.io/step-by-step-building-and-publishing-an-npm-typescript-package-44fe7164964c
1. Selecting text nodes: https://javascript.info/selection-range

### Node.js

1. `npm install -g npm-check-updates` -> `ncu` -> update dependencies!
1. [Best architecture guide](https://softwareontheroad.com/ideal-nodejs-project-structure/)
1. [Optimize](https://community.risingstack.com/how-to-find-node-js-performance-optimization-killers/)
1. [Child process](https://medium.freecodecamp.org/node-js-child-processes-everything-you-need-to-know-e69498fe970a)
1. [CLI tool](https://developer.atlassian.com/blog/2015/11/scripting-with-node/)
1. Error handling: 
    - Express error handling: https://expressjs.com/en/guide/error-handling.html
    - https://thecodebarbarian.com/80-20-guide-to-express-error-handling
7) [Events](https://nodejs.org/api/events.html)
8) [Case Converter](https://www.npmjs.com/package/change-case) `npm install change-case --save`

### React

1. [JSFiddle](https://jsfiddle.net/reactjs/69z2wepo/)
1. [Conditional renderings](https://www.robinwieruch.de/conditional-rendering-react/)
1. robinwieruch:
    - https://www.robinwieruch.de/react-render-props
    - https://www.robinwieruch.de/react-hooks-fetch-data
1. Redux:
    - [Example](https://blog.tylerbuchea.com/super-simple-react-redux-application-example/)
    - [Immutable patterns](https://redux.js.org/docs/recipes/reducers/ImmutableUpdatePatterns.html)
    - [Async actions](https://redux.js.org/advanced/async-actions)
    
```javascript
useEffect(() => console.log("mount"), []);
useEffect(() => console.log("will update data"), [data]);
useEffect(() => console.log("will update any"));
useEffect(() => () => console.log("will update data or unmount"), [data]);
useEffect(() => () => console.log("unmount"), []);
```
