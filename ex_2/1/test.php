<?php

require_once('../_helpers/strip.php');

// https://depthsecurity.com/blog/exploitation-xml-external-entity-xxe-injection

libxml_disable_entity_loader (false);

$xml = strlen($_GET['xml']) > 0 ? $_GET['xml'] : '<root><content>No XML found</content></root>';

$document = new DOMDocument();
$document->loadXML($xml, LIBXML_DTDLOAD); # https://www.php.net/manual/en/libxml.constants.php : LIBXML_NOENT Caution Enabling entity substitution may facilitate XML External Entity (XXE) attacks.
$parsedDocument = simplexml_import_dom($document);

echo $parsedDocument->content;
