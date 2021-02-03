import React, { useRef, useEffect, useState } from 'react'
import 'style.css'

const DropDownMenu = ({ children }) => {
  const [showing, setShowing] = useState(false)

  const showMenu = useRef(null)
  const windowClick = e => {
    if (showMenu && e.target === showMenu.current) setShowing(!showing)
    else if (showing) setShowing(false)
  }
  useEffect(() => {
    window.addEventListener('click', windowClick)
    return () => {
      window.removeEventListener('click', windowClick)
    }
  })

  return (
    <div className={'drop-down-menu'} style={{ position: 'relative' }}>
      <button className={'toggle-button'} ref={showMenu}>
        ⋮
      </button>
      {showing && <div className={'menu-items'}>{children}</div>}
    </div>
  )
}
