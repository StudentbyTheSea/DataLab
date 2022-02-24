"use strict";(self.webpackChunkmy_website=self.webpackChunkmy_website||[]).push([[506],{3905:function(e,t,n){n.d(t,{Zo:function(){return p},kt:function(){return d}});var a=n(7294);function r(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function i(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,a)}return n}function o(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?i(Object(n),!0).forEach((function(t){r(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):i(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function s(e,t){if(null==e)return{};var n,a,r=function(e,t){if(null==e)return{};var n,a,r={},i=Object.keys(e);for(a=0;a<i.length;a++)n=i[a],t.indexOf(n)>=0||(r[n]=e[n]);return r}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(a=0;a<i.length;a++)n=i[a],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(r[n]=e[n])}return r}var c=a.createContext({}),l=function(e){var t=a.useContext(c),n=t;return e&&(n="function"==typeof e?e(t):o(o({},t),e)),n},p=function(e){var t=l(e.components);return a.createElement(c.Provider,{value:t},e.children)},f={inlineCode:"code",wrapper:function(e){var t=e.children;return a.createElement(a.Fragment,{},t)}},u=a.forwardRef((function(e,t){var n=e.components,r=e.mdxType,i=e.originalType,c=e.parentName,p=s(e,["components","mdxType","originalType","parentName"]),u=l(n),d=r,h=u["".concat(c,".").concat(d)]||u[d]||f[d]||i;return n?a.createElement(h,o(o({ref:t},p),{},{components:n})):a.createElement(h,o({ref:t},p))}));function d(e,t){var n=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var i=n.length,o=new Array(i);o[0]=u;var s={};for(var c in t)hasOwnProperty.call(t,c)&&(s[c]=t[c]);s.originalType=e,s.mdxType="string"==typeof e?e:r,o[1]=s;for(var l=2;l<i;l++)o[l]=n[l];return a.createElement.apply(null,o)}return a.createElement.apply(null,n)}u.displayName="MDXCreateElement"},247:function(e,t,n){n.r(t),n.d(t,{frontMatter:function(){return s},contentTitle:function(){return c},metadata:function(){return l},toc:function(){return p},default:function(){return u}});var a=n(7462),r=n(3366),i=(n(7294),n(3905)),o=["components"],s={},c="Hate Speech Analysis",l={unversionedId:"WebUI/bias_analysis_for_hate_speech",id:"WebUI/bias_analysis_for_hate_speech",title:"Hate Speech Analysis",description:"DataLab supports different types of bias analyses for datasets and hate speech is one case.",source:"@site/docs/WebUI/3_bias_analysis_for_hate_speech.md",sourceDirName:"WebUI",slug:"/WebUI/bias_analysis_for_hate_speech",permalink:"/DataLab/docs/WebUI/bias_analysis_for_hate_speech",editUrl:"https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/docs/WebUI/3_bias_analysis_for_hate_speech.md",tags:[],version:"current",sidebarPosition:3,frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Fine-grained Information of a Dataset",permalink:"/DataLab/docs/WebUI/fine_grained_analysis_of_a_dataset"},next:{title:"Gender Bias Analysis",permalink:"/DataLab/docs/WebUI/bias_analysis_for_gender_bias"}},p=[{value:"1. Dataset Selection",id:"1-dataset-selection",children:[],level:3},{value:"2. Choose the <code>hate speech</code> filter",id:"2-choose-the-hate-speech-filter",children:[],level:3}],f={toc:p};function u(e){var t=e.components,n=(0,r.Z)(e,o);return(0,i.kt)("wrapper",(0,a.Z)({},f,n,{components:t,mdxType:"MDXLayout"}),(0,i.kt)("h1",{id:"hate-speech-analysis"},"Hate Speech Analysis"),(0,i.kt)("p",null,"DataLab supports different types of bias analyses for datasets and ",(0,i.kt)("inlineCode",{parentName:"p"},"hate speech")," is one case.\nSpecifically, given a dataset, DataLab can identify what percentage of samples contains hate speech words.\nAlthough deciding whether a sentence contains toxic language is a slightly complex task, which may involve the confounding effects of\ndialect and the social identity of a speaker ",(0,i.kt)("a",{parentName:"p",href:"https://aclanthology.org/P19-1163.pdf"},"Sap et al. (2019)"),", we make a first step by following ",(0,i.kt)("a",{parentName:"p",href:"https://aaai.org/ocs/index.php/ICWSM/ICWSM17/paper/view/15665"},"Davidson et al (2017)"),",\nclassifying the samples into following categories:"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("inlineCode",{parentName:"li"},"hate speech")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("inlineCode",{parentName:"li"},"offensive language")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("inlineCode",{parentName:"li"},"neither"))),(0,i.kt)("p",null,"We then calculate the ratio of samples in different categories."),(0,i.kt)("p",null,"To perform this type of analysis:"),(0,i.kt)("h3",{id:"1-dataset-selection"},"1. Dataset Selection"),(0,i.kt)("p",null,"You just need to choose a dataset and click the right mouse button, and choose ",(0,i.kt)("inlineCode",{parentName:"p"},"analysis")," -> ",(0,i.kt)("inlineCode",{parentName:"p"},"bias"),", then you will enter into a page designed for bias analysis"),(0,i.kt)("img",{src:"https://user-images.githubusercontent.com/59123869/155384702-9c7dc15b-036f-4ce4-906d-1258075dad8a.png",width:"200"}),(0,i.kt)("h3",{id:"2-choose-the-hate-speech-filter"},"2. Choose the ",(0,i.kt)("inlineCode",{parentName:"h3"},"hate speech")," filter"),(0,i.kt)("p",null,"As shown below, different colors represent the proportions of samples with different categories (",(0,i.kt)("inlineCode",{parentName:"p"},"hate speech"),", ",(0,i.kt)("inlineCode",{parentName:"p"},"offensive language")," and ",(0,i.kt)("inlineCode",{parentName:"p"},"neither"),")"),(0,i.kt)("img",{src:"https://user-images.githubusercontent.com/59123869/155385027-17d4246b-2551-4ce2-9d31-b6305433ad08.png",width:"600"}))}u.isMDXComponent=!0}}]);