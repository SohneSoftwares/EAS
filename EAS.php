<?php
class EAS {
    
    private $letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789_- ';
    
    public function encode($original, $salto) {
        $new_string = '';
        $original = str_split($original, 1);
        foreach($original as $item) {
            $index = strpos($this->letras, $item);
            if (($index + $salto) >= strlen($this->letras)) {
                $index = ($index + $salto) - strlen($this->letras);
            } else {
                $index += $salto;
            }
            $new_string .= $this->letras{$index};
        }
        return $new_string;
    }
    
    public function decode($original, $salto) {
        $new_string = '';
        $original = str_split($original, 1);
        foreach($original as $item) {
            $index = strpos($this->letras, $item);
            if (($index - $salto) < 0) {
                $index = ($index - $salto) + strlen($this->letras);
            } else if (($index - $salto) == 0) { 
                $index = 0;
            } else {
                $index -= $salto;
            }
            $new_string .= $this->letras{$index};
        }
        
        return $new_string;
    }
}
?>
