{-# LANGUAGE TemplateHaskell, QuasiQuotes, OverloadedStrings #-}
module Main where

import           Control.Applicative
import           Snap.Core
import           Snap.Util.FileServe
import           Snap.Http.Server
import           Text.Hamlet hiding (renderHtml)
import           Text.Blaze.Html.Renderer.String (renderHtml)
import           Data.Text (pack)
import qualified Data.ByteString.Char8 (pack)

data Url = Home | Spells
data Spell = MagicMissile | Darkness | Fireball

renderUrl Home _ = "http://localhost:8000/"
renderUrl Spells   _ = "http://localhost:8000/spells"

renderSpell MagicMissile _ = "Magic Missile deals good damage"
renderSpell Darkness _ = "Darkness makes it hard to see"
renderSpell Fireball _ = "Fireball serves tea for NONE"


title = pack "Super Awesome Website"

home :: HtmlUrl Url
home = [hamlet|
<html>
    <head>
        #{title}
    
        <p>
            <a href=@{Home}>Home
            <a href=@{Spells}>Spells
    <body>
|]

spellList :: HtmlUrl Spell
spellList = [hamlet|
<html>
    <head>
    <body>
    <ul>
        <li> @{MagicMissile}
        <li> @{Darkness}
        <li> @{Fireball}
|]


main :: IO ()
main = quickHttpServe site

site :: Snap ()
site =
    ifTop (homeHandler) <|>
    route [ ("spells", spellHandler)
          ] <|>
    dir "static" (serveDirectory ".")

homeHandler :: Snap ()
homeHandler = do
    let html = home renderUrl
    writeBS $ Data.ByteString.Char8.pack $ renderHtml html

spellHandler :: Snap ()
spellHandler = do
    let html = home renderUrl
    writeBS $ Data.ByteString.Char8.pack $ renderHtml html
    let html2 = spellList renderSpell
    writeBS $ Data.ByteString.Char8.pack $ renderHtml html2




