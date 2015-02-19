import            Heist
import            Heist.Interpreted
import qualified  Data.Text as T
import qualified  Text.XmlHtml as X

factSplice :: Splice Snap
factSplice = do
    input <- getParamNode
    let text = T.unpack $ X.nodeText input
        n = read text :: Int
    return [X.TextNode $ T.pack $ show $ product [1..n]]